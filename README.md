# Building with the Claude API

This repository contains hands-on exercises and examples from the [Anthropic course: Building with the Claude API](https://github.com/anthropics/courses/tree/master).

## Modules

### Module 1: Accessing Claude with the API

📁 [`001-Accessing-Claude_with-the-API/`](./001-Accessing-Claude_with-the-API/)

Learn the fundamentals of interacting with Claude through the Anthropic API.

| Notebook | Description |
|----------|-------------|
| [`001_requests.ipynb`](./001-Accessing-Claude_with-the-API/001_requests.ipynb) | Basic API requests, message handling, and multi-turn conversations |
| [`001_requests_exercise.ipynb`](./001-Accessing-Claude_with-the-API/001_requests_exercise.ipynb) | Build an interactive chatbot using the messages API |
| [`002_system_prompt.ipynb`](./001-Accessing-Claude_with-the-API/002_system_prompt.ipynb) | Using system prompts to guide Claude's behavior |
| [`002_system_prompt_exercise.ipynb`](./001-Accessing-Claude_with-the-API/002_system_prompt_exercise.ipynb) | Create a concise Python code assistant with system prompts |
| [`003_temperature.ipynb`](./001-Accessing-Claude_with-the-API/003_temperature.ipynb) | Controlling output randomness with the temperature parameter |
| [`004_streaming.ipynb`](./001-Accessing-Claude_with-the-API/004_streaming.ipynb) | Real-time response streaming and handling stream events |
| [`005_controlling_output.ipynb`](./001-Accessing-Claude_with-the-API/005_controlling_output.ipynb) | Message prefilling, stop sequences, and structured output (JSON) |

### Module 2: Prompt Evaluation

📁 [`002-Prompt-evaluation/`](./002-Prompt-evaluation/)

Learn how to systematically evaluate and grade prompt outputs using datasets, model-based grading, and code-based validation.

| Notebook | Description |
|----------|-------------|
| [`001_generating_dataset.ipynb`](./002-Prompt-evaluation/001_generating_dataset.ipynb) | Generate evaluation datasets for testing prompts |
| [`002_running_eval.ipynb`](./002-Prompt-evaluation/002_running_eval.ipynb) | Run evaluations across test cases and collect results |
| [`003_model_based_grading.ipynb`](./002-Prompt-evaluation/003_model_based_grading.ipynb) | Use Claude to grade and evaluate AI-generated solutions |
| [`004_code_based_grading.ipynb`](./002-Prompt-evaluation/004_code_based_grading.ipynb) | Combine syntax validation (JSON, Python, Regex) with model grading |
| [`005_exercise.ipynb`](./002-Prompt-evaluation/005_exercise.ipynb) | Exercise: Enhance the model grader with solution criteria |

### Module 3: Prompt Engineering Techniques

📁 [`003-Prompt-engineering/`](./003-Prompt-engineering/)

Master essential prompt engineering techniques to improve Claude's output quality, consistency, and accuracy.

| Notebook | Description |
|----------|-------------|
| [`001_prompting.ipynb`](./003-Prompt-engineering/001_prompting.ipynb) | Introduction to prompt engineering with the PromptEvaluator framework |
| [`002_being_clear_direct.ipynb`](./003-Prompt-engineering/002_being_clear_direct.ipynb) | Writing clear and direct prompts for better results |
| [`003_being_specific.ipynb`](./003-Prompt-engineering/003_being_specific.ipynb) | Using guidelines and step-by-step instructions for complex tasks |
| [`004_xml.ipynb`](./003-Prompt-engineering/004_xml.ipynb) | Structuring prompts with XML tags for clarity and organization |
| [`005_providing_examples.ipynb`](./003-Prompt-engineering/005_providing_examples.ipynb) | One-shot and multi-shot examples to guide model behavior |
| [`006_prompting_exercise.ipynb`](./003-Prompt-engineering/006_prompting_exercise.ipynb) | Exercise: Extract topics from scholarly articles |

### Module 4: Tool Use with Claude

📁 [`004-Tool-use-with-Claude/`](./004-Tool-use-with-Claude/)

Learn how to extend Claude's capabilities by defining tools, handling tool calls, and building multi-turn agentic workflows.

| Notebook | Description |
|----------|-------------|
| [`001_tools_function.ipynb`](./004-Tool-use-with-Claude/001_tools_function.ipynb) | Introduction to tool functions for accessing real-time information |
| [`002_tools_schemas.ipynb`](./004-Tool-use-with-Claude/002_tools_schemas.ipynb) | Creating JSON schemas to define tool arguments |
| [`003_tools_handling_message_blocks.ipynb`](./004-Tool-use-with-Claude/003_tools_handling_message_blocks.ipynb) | Handling multi-block messages with text and tool use content |
| [`004_tools_sending_tool_results.ipynb`](./004-Tool-use-with-Claude/004_tools_sending_tool_results.ipynb) | Executing functions and sending results back to Claude |
| [`005_tools_multi-turn-conversations.ipynb`](./004-Tool-use-with-Claude/005_tools_multi-turn-conversations.ipynb) | Calling multiple tools in sequence to answer a single question |
| [`006_tools_implementing_multiple_turns.ipynb`](./004-Tool-use-with-Claude/006_tools_implementing_multiple_turns.ipynb) | Building a conversation loop that runs until tool use completes |
| [`007_tools_using_multiple_tools.ipynb`](./004-Tool-use-with-Claude/007_tools_using_multiple_tools.ipynb) | Integrating multiple tools into a single implementation |
| [`008_tools_batch_tools.ipynb`](./004-Tool-use-with-Claude/008_tools_batch_tools.ipynb) | Running multiple tool calls in parallel within a single message |
| [`009_tools_structured_data.ipynb`](./004-Tool-use-with-Claude/009_tools_structured_data.ipynb) | Using tools to extract structured data reliably |
| [`010_tools_fine_grained_tool_calling.ipynb`](./004-Tool-use-with-Claude/010_tools_fine_grained_tool_calling.ipynb) | Combining tool use with streaming for real-time updates |
| [`011_tools_text_edit.ipynb`](./004-Tool-use-with-Claude/011_tools_text_edit.ipynb) | Using Claude's built-in text editor tool for file operations |
| [`012_tools_web_search.ipynb`](./004-Tool-use-with-Claude/012_tools_web_search.ipynb) | Enabling Claude's built-in web search tool for current information |

### Module 5: Retrieval-Augmented Generation (RAG)

📁 [`005-Retrieval-Augmented-Generation/`](./005-Retrieval-Augmented-Generation/)

Build RAG pipelines from scratch, covering chunking strategies, embeddings, vector search, lexical search, and advanced retrieval techniques.

> **Additional setup required for this module:**
> - Install the Voyage AI package: `pip install voyageai`
> - Add your Voyage AI API key to `.env`: `VOYAGE_API_KEY="your_key_here"` ([Get one here](https://dash.voyageai.com/))

| Notebook | Description |
|----------|-------------|
| [`001_introducing-RAG.ipynb`](./005-Retrieval-Augmented-Generation/001_introducing-RAG.ipynb) | Text chunking strategies: size-based, structure-based, and semantic-based |
| [`002_embeddings.ipynb`](./005-Retrieval-Augmented-Generation/002_embeddings.ipynb) | Generating text embeddings for semantic search over document chunks |
| [`003_vectordb.ipynb`](./005-Retrieval-Augmented-Generation/003_vectordb.ipynb) | Complete RAG flow with chunking, embeddings, vector storage, and similarity search |
| [`004_bm25.ipynb`](./005-Retrieval-Augmented-Generation/004_bm25.ipynb) | BM25 lexical search as a complement to semantic search |
| [`005_hybrid.ipynb`](./005-Retrieval-Augmented-Generation/005_hybrid.ipynb) | Hybrid search combining semantic and lexical retrieval with Reciprocal Rank Fusion |
| [`006_reranking.ipynb`](./005-Retrieval-Augmented-Generation/006_reranking.ipynb) | Reranking retrieved documents with Claude for improved accuracy |
| [`007_contextual.ipynb`](./005-Retrieval-Augmented-Generation/007_contextual.ipynb) | Contextual retrieval to preserve document context in chunked passages |

### Module 6: Features of Claude

📁 [`006-Feature-of-Claude/`](./006-Feature-of-Claude/)

Explore Claude's advanced built-in features including extended thinking, vision, PDF processing, citations, caching, and code execution.

| Notebook | Description |
|----------|-------------|
| [`001_thinking.ipynb`](./006-Feature-of-Claude/001_thinking.ipynb) | Extended thinking for complex reasoning before generating responses |
| [`002_images.ipynb`](./006-Feature-of-Claude/002_images.ipynb) | Vision capabilities for analyzing and understanding images |
| [`003_pdf.ipynb`](./006-Feature-of-Claude/003_pdf.ipynb) | Reading and analyzing PDF files for document processing |
| [`004_citations.ipynb`](./006-Feature-of-Claude/004_citations.ipynb) | Citations to trace answers back to specific source locations |
| [`005_caching.ipynb`](./006-Feature-of-Claude/005_caching.ipynb) | Prompt caching to speed up responses and reduce costs |
| [`006_code_execution.ipynb`](./006-Feature-of-Claude/006_code_execution.ipynb) | Files API and code execution for delegating complex tasks |

## Setup

### Prerequisites

- Python 3.8+
- An Anthropic API key ([Get one here](https://console.anthropic.com/))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jaygaha/Building-with-the-Claude-API.git
   cd Building-with-the-Claude-API
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your API key:
   ```bash
   cp .env-example .env
   ```
   Then edit `.env` and add your Anthropic API key.

5. Launch Jupyter:
   ```bash
   jupyter notebook
   ```

## Resources

- [Anthropic API Documentation](https://docs.anthropic.com/)
- [Claude API Reference](https://docs.anthropic.com/en/api/getting-started)
- [Anthropic Courses](https://github.com/anthropics/courses)
