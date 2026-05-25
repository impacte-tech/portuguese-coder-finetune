// Portuguese Coder - Main Application
// Features: Transformers.js + Pyodide REPL + Self-Correction

class PortugueseCoderApp {
    constructor() {
        this.model = null;
        this.tokenizer = null;
        this.pyodide = null;
        this.currentQuestion = null;
        this.conversationHistory = [];
        this.executionAttempts = 0;
        this.maxRetries = 3;
        
        this.init();
    }

    async init() {
        this.setupUI();
        this.loadQuestions();
        
        // Load model and Python in parallel
        await Promise.all([
            this.loadModel(),
            this.loadPyodide()
        ]);
    }

    setupUI() {
        // DOM elements
        this.questionsList = document.getElementById('questions-list');
        this.questionDisplay = document.getElementById('question-display');
        this.userInput = document.getElementById('user-input');
        this.modelOutput = document.getElementById('model-output');
        this.replOutput = document.getElementById('repl-output');
        this.replInput = document.getElementById('repl-input');
        this.executionLog = document.getElementById('execution-log');
        this.modelStatus = document.getElementById('model-status');
        this.pyodideStatus = document.getElementById('pyodide-status');
        
        // Buttons
        document.getElementById('ask-btn').addEventListener('click', () => this.askModel());
        document.getElementById('run-repl-btn').addEventListener('click', () => this.runInREPL());
        document.getElementById('retry-btn').addEventListener('click', () => this.retryWithError());
        document.getElementById('clear-repl').addEventListener('click', () => this.clearREPL());
        document.getElementById('test-solution').addEventListener('click', () => this.testSolution());
        
        // REPL input
        this.replInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.executeREPLCommand(this.replInput.value);
                this.replInput.value = '';
            }
        });
        
        // Search and filter
        document.getElementById('search-input').addEventListener('input', (e) => {
            this.filterQuestions(e.target.value, document.getElementById('category-filter').value);
        });
        document.getElementById('category-filter').addEventListener('change', (e) => {
            this.filterQuestions(document.getElementById('search-input').value, e.target.value);
        });
    }

    loadQuestions() {
        this.questionsList.innerHTML = '';
        blind75Questions.forEach(q => {
            const item = document.createElement('div');
            item.className = 'question-item';
            item.dataset.id = q.id;
            item.innerHTML = `
                <div class="title">${q.id}. ${q.title}</div>
                <div class="category">${q.category} • ${q.difficulty}</div>
            `;
            item.addEventListener('click', () => this.selectQuestion(q));
            this.questionsList.appendChild(item);
        });
    }

    filterQuestions(search, category) {
        const items = this.questionsList.querySelectorAll('.question-item');
        items.forEach(item => {
            const q = blind75Questions.find(q => q.id == item.dataset.id);
            const matchesSearch = !search || q.title.toLowerCase().includes(search.toLowerCase());
            const matchesCategory = category === 'all' || q.category === category;
            item.style.display = matchesSearch && matchesCategory ? 'block' : 'none';
        });
    }

    selectQuestion(question) {
        this.currentQuestion = question;
        this.executionAttempts = 0;
        
        // Update UI
        document.querySelectorAll('.question-item').forEach(item => {
            item.classList.toggle('active', item.dataset.id == question.id);
        });
        
        // Display question
        this.questionDisplay.innerHTML = `
            <h3>${question.id}. ${question.title}</h3>
            <div class="description">
                <p><strong>Categoria:</strong> ${question.category} | <strong>Dificuldade:</strong> ${question.difficulty}</p>
                <p>${question.description}</p>
            </div>
            <div class="example">
                <strong>Exemplo:</strong><br>
                <pre>${question.example}</pre>
            </div>
            <div class="hints">
                <strong>Dicas:</strong>
                <ul>${question.hints.map(h => `<li>${h}</li>`).join('')}</ul>
            </div>
        `;
        
        // Set default user input
        this.userInput.value = `Resolva este problema: ${question.title}\n\n${question.description}`;
        
        // Enable buttons
        this.updateButtonStates();
        
        this.log('Questão selecionada', `${question.title}`);
    }

    async loadModel() {
        try {
            this.modelStatus.textContent = '⏳ Baixando Qwen2.5-Coder-0.5B...';
            
            // Load transformers pipeline for text generation
            const { pipeline } = window.transformers;
            
            this.generator = await pipeline(
                'text-generation',
                'Xenova/Qwen2.5-Coder-0.5B-Instruct',
                {
                    dtype: 'q4',  // Quantized for faster loading
                    device: 'webgpu',  // Use GPU if available
                }
            );
            
            this.modelStatus.textContent = '✅ Modelo pronto';
            this.modelStatus.classList.add('ready');
            this.updateButtonStates();
            
            this.log('Modelo', 'Qwen2.5-Coder-0.5B carregado com sucesso');
        } catch (error) {
            this.modelStatus.textContent = '❌ Erro ao carregar modelo';
            console.error('Model loading error:', error);
            this.log('Erro', `Falha ao carregar modelo: ${error.message}`);
        }
    }

    async loadPyodide() {
        try {
            this.pyodideStatus.textContent = '⏳ Carregando Pyodide...';
            
            this.pyodide = await loadPyodide();
            
            // Install common packages
            await this.pyodide.loadPackage(['numpy']);
            
            this.pyodideStatus.textContent = '✅ Python pronto';
            this.pyodideStatus.classList.add('ready');
            this.replInput.disabled = false;
            this.updateButtonStates();
            
            this.log('Python', 'Pyodide carregado com sucesso');
        } catch (error) {
            this.pyodideStatus.textContent = '❌ Erro ao carregar Python';
            console.error('Pyodide loading error:', error);
        }
    }

    updateButtonStates() {
        const modelReady = this.generator !== null;
        const pythonReady = this.pyodide !== null;
        const hasQuestion = this.currentQuestion !== null;
        
        document.getElementById('ask-btn').disabled = !modelReady || !hasQuestion;
        document.getElementById('run-repl-btn').disabled = !pythonReady;
        document.getElementById('retry-btn').disabled = !modelReady || this.executionAttempts === 0;
    }

    async askModel() {
        if (!this.generator || !this.currentQuestion) return;
        
        const userPrompt = this.userInput.value;
        this.modelOutput.innerHTML = '<div class="loading"></div> Gerando resposta...';
        
        try {
            // Build conversation
            const messages = [
                {
                    role: 'system',
                    content: `Você é um assistente de programação Python para estudantes brasileiros. 
Responda em português. Forneça código Python funcional e explicações claras.
Quando gerar código, certifique-se de que está sintaticamente correto.`
                },
                {
                    role: 'user',
                    content: userPrompt
                }
            ];
            
            // Generate response
            const output = await this.generator(messages, {
                max_new_tokens: 512,
                temperature: 0.7,
                do_sample: true,
                top_p: 0.95,
            });
            
            const response = output[0].generated_text[output[0].generated_text.length - 1].content;
            this.lastModelResponse = response;
            
            // Display with formatting
            this.displayModelResponse(response);
            
            this.log('Modelo', 'Resposta gerada');
            
            // Auto-extract and run code if present
            const code = this.extractCode(response);
            if (code && this.pyodide) {
                this.log('Auto-exec', 'Código detectado, executando no REPL...');
                await this.executeCodeInREPL(code);
            }
            
        } catch (error) {
            this.modelOutput.innerHTML = `<div class="error">Erro: ${error.message}</div>`;
            this.log('Erro', `Geração falhou: ${error.message}`);
        }
    }

    displayModelResponse(response) {
        // Simple markdown-like formatting
        let formatted = response
            .replace(/```python\n([\s\S]*?)```/g, '<div class="code"><pre>$1</pre></div>')
            .replace(/```\n([\s\S]*?)```/g, '<div class="code"><pre>$1</pre></div>')
            .replace(/`([^`]+)`/g, '<code>$1</code>')
            .replace(/\n\n/g, '<br><br>');
        
        this.modelOutput.innerHTML = formatted;
    }

    extractCode(response) {
        // Extract code blocks from response
        const codeBlockMatch = response.match(/```python\n([\s\S]*?)```/);
        if (codeBlockMatch) {
            return codeBlockMatch[1].trim();
        }
        
        // Try without language specifier
        const genericCodeMatch = response.match(/```\n([\s\S]*?)```/);
        if (genericCodeMatch) {
            return genericCodeMatch[1].trim();
        }
        
        return null;
    }

    async runInREPL() {
        const code = this.extractCode(this.modelOutput.textContent);
        if (code) {
            await this.executeCodeInREPL(code);
        } else {
            this.appendToREPL('Nenhum código encontrado na resposta', 'error');
        }
    }

    async executeCodeInREPL(code) {
        if (!this.pyodide) return;
        
        this.executionAttempts++;
        this.appendToREPL(`>>> # Tentativa ${this.executionAttempts}`, 'input');
        
        try {
            // Capture output
            let output = '';
            
            // Redirect stdout
            this.pyodide.setStdout({ batched: (text) => { output += text; } });
            
            // Execute code
            await this.pyodide.runPythonAsync(code);
            
            // Display output
            if (output) {
                this.appendToREPL(output, 'output');
                this.log('Execução', `Sucesso (tentativa ${this.executionAttempts})`);
                
                // Check if output matches expected
                if (this.currentQuestion) {
                    await this.validateOutput(output);
                }
            } else {
                this.appendToREPL('(sem saída)', 'output');
            }
            
        } catch (error) {
            const errorMsg = error.message;
            this.appendToREPL(`Erro: ${errorMsg}`, 'error');
            this.log('Erro', `Execução falhou: ${errorMsg}`);
            
            // Auto-retry if we haven't exceeded max retries
            if (this.executionAttempts < this.maxRetries) {
                await this.retryWithError(errorMsg);
            }
        }
        
        this.updateButtonStates();
    }

    async executeREPLCommand(command) {
        if (!command.trim()) return;
        
        this.appendToREPL(`>>> ${command}`, 'input');
        
        try {
            let output = '';
            this.pyodide.setStdout({ batched: (text) => { output += text; } });
            
            const result = await this.pyodide.runPythonAsync(command);
            
            if (output) {
                this.appendToREPL(output, 'output');
            } else if (result !== undefined) {
                this.appendToREPL(String(result), 'output');
            }
        } catch (error) {
            this.appendToREPL(`Erro: ${error.message}`, 'error');
        }
    }

    async retryWithError(errorMsg = null) {
        if (!this.generator || !this.currentQuestion) return;
        
        const lastError = errorMsg || 'O código anterior teve um erro';
        
        this.modelOutput.innerHTML += `
            <div class="thinking">
                🔄 Tentativa ${this.executionAttempts + 1}/${this.maxRetries}: Corrigindo erro...
            </div>
        `;
        
        const retryPrompt = `O código anterior teve este erro: "${lastError}". 

Por favor, corrija o código para resolver o problema: "${this.currentQuestion.title}".

Forneça apenas o código corrigido, sem explicações adicionais.`;
        
        try {
            const messages = [
                { role: 'system', content: 'Você é um assistente de programação. Corrija o código fornecido.' },
                { role: 'user', content: retryPrompt }
            ];
            
            const output = await this.generator(messages, {
                max_new_tokens: 512,
                temperature: 0.5,  // Lower temperature for more focused fix
            });
            
            const fixedCode = output[0].generated_text[output[0].generated_text.length - 1].content;
            this.lastModelResponse = fixedCode;
            
            this.displayModelResponse(fixedCode);
            this.log('Retry', `Tentativa ${this.executionAttempts + 1} com correção`);
            
            // Auto-run the fixed code
            const code = this.extractCode(fixedCode);
            if (code) {
                await this.executeCodeInREPL(code);
            }
            
        } catch (error) {
            this.log('Erro', `Retry falhou: ${error.message}`);
        }
    }

    async validateOutput(output) {
        // Simple validation against expected output
        if (!this.currentQuestion.testCases) return;
        
        const expected = this.currentQuestion.testCases[0].expected;
        
        // Normalize for comparison
        const normalizedOutput = output.trim().replace(/\s+/g, ' ');
        const normalizedExpected = expected.trim().replace(/\s+/g, ' ');
        
        if (normalizedOutput.includes(normalizedExpected) || normalizedExpected.includes(normalizedOutput)) {
            this.appendToREPL('✅ Saída corresponde ao esperado!', 'success');
            this.log('Validação', 'Saída correta!');
        } else {
            this.appendToREPL(`⚠️ Saída diferente do esperado. Esperado: ${expected}`, 'error');
        }
    }

    async testSolution() {
        if (!this.currentQuestion || !this.pyodide) return;
        
        this.appendToREPL('=== Testando Solução ===', 'input');
        
        for (const testCase of this.currentQuestion.testCases) {
            this.appendToREPL(`Teste: ${testCase.input}`, 'input');
            
            try {
                let output = '';
                this.pyodide.setStdout({ batched: (text) => { output += text; } });
                
                await this.pyodide.runPythonAsync(testCase.input);
                
                const passed = output.trim().includes(testCase.expected.trim());
                this.appendToREPL(
                    `${passed ? '✅' : '❌'} Saída: ${output.trim()} (Esperado: ${testCase.expected})`,
                    passed ? 'success' : 'error'
                );
            } catch (error) {
                this.appendToREPL(`❌ Erro: ${error.message}`, 'error');
            }
        }
    }

    appendToREPL(text, type) {
        const line = document.createElement('div');
        line.className = `${type}-line`;
        line.textContent = text;
        this.replOutput.appendChild(line);
        this.replOutput.scrollTop = this.replOutput.scrollHeight;
    }

    clearREPL() {
        this.replOutput.innerHTML = '';
        this.executionAttempts = 0;
        this.log('REPL', 'Console limpo');
    }

    log(action, details) {
        const entry = document.createElement('div');
        entry.className = 'log-entry';
        const timestamp = new Date().toLocaleTimeString();
        entry.innerHTML = `
            <span class="timestamp">[${timestamp}]</span>
            <span class="action">${action}:</span> ${details}
        `;
        this.executionLog.appendChild(entry);
        this.executionLog.scrollTop = this.executionLog.scrollHeight;
    }
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.app = new PortugueseCoderApp();
});
