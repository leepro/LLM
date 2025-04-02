# "Nitty-gritty" of LLM

## Basics of LLM

* Tokenizer
* Small models: GPT2

## Fine-tuning

* Unsloth + Gemma3 4B + SFT

## Hardwares

* GPU
  * NVIDIA

| Architecture | Release Year | Process Node | Notable GPUs | Key Features |
|-------------|-------------|--------------|--------------|--------------|
| **Tesla**   | 2006        | 90nm, 65nm   | GeForce 8, Tesla C870 | First CUDA architecture, G80 core |
| **Fermi**   | 2010        | 40nm         | GTX 400/500, Tesla M2090 | Unified memory, ECC support |
| **Kepler**  | 2012        | 28nm         | GTX 600/700, Tesla K40 | Dynamic Parallelism, GPU Boost |
| **Maxwell** | 2014        | 28nm         | GTX 900, Tesla M40 | Improved efficiency, NVENC support |
| **Pascal**  | 2016        | 16nm         | GTX 10 series, Tesla P100 | FP16 support, NVLink introduced |
| **Volta**   | 2017        | 12nm         | Tesla V100 | First Tensor Cores, Deep Learning optimized |
| **Turing**  | 2018        | 12nm         | RTX 20 series, T4 | First RT Cores, AI-powered DLSS |
| **Ampere**  | 2020        | 8nm          | RTX 30 series, A100 | 2nd-gen RT & Tensor Cores, FP32 boost |
| **Hopper**  | 2022        | 4nm          | H100 | Transformer Engine, NVLink 4.0 |
| **Ada Lovelace** | 2022 | 4nm | RTX 40 series | 3rd-gen RT Cores, DLSS 3 |
| **Blackwell** | 2024 | 3nm (expected) | B100 (expected) | Next-gen AI acceleration |

  * AMD Instinct MI300X, MI250X

 TPU
  * Google

| TPU Version | Release Year | Performance (TFLOPS) | Memory (HBM) | Use Cases |
|------------|-------------|----------------------|--------------|-----------|
| **TPU v1** | 2015        | 92                   | 8GB          | Early TensorFlow acceleration |
| **TPU v2** | 2017        | 180                  | 16GB         | Cloud TPU, ResNet, GNMT |
| **TPU v3** | 2018        | 420                  | 32GB         | BERT, Transformer training |
| **TPU v4** | 2021        | 1000+                | 32GB         | Large-scale LLM training, Google Cloud |
| **TPU v5** | 2023        | Unreleased (Improved over TPU v4) | 32GB+ | Gemini AI, ultra-large models |

* Cerebras Wafer-Scale Engine (WSE): Ideal for large-scale AI, including LLMs, used in research for models requiring massive parallelism (seo.ai blog on AI chip makers).
* Graphcore Intelligence Processing Unit (IPU): Optimized for AI training and inference, suitable for LLMs in cloud and data centers (seo.ai blog on AI chip makers).
* SambaNova Reconfigurable Dataflow Processing Unit (RDPU): Efficient for both training and inference, catering to LLM workloads in enterprise settings (seo.ai blog on AI chip makers).
* Groq Tensor Streaming Processor (TSP): Focused on ultra-low latency inference for LLMs, with up to 10x energy efficiency, ideal for real-time applications (Groq products).
* AWS Offerings: Trainium2 and Inferentia2 cater to AWS’s cloud ecosystem, with Trainium2 offering 30-40% better price performance for training and Inferentia2 up to 4X throughput for inference, supporting LLMs in Amazon SageMaker and EC2, reflecting AWS’s focus on scalable AI solutions.
* Tenstorrent: a company that designs and manufactures AI hardware and software solutions, offering products like the Grayskull and Wormhole processors for scalable deep learning and machine learning applications. 

* Apple Silicon
  * MLX

| Chip | Release Year | Neural Engine (TOPS) | GPU Cores | Notable ML Features |
|------|-------------|----------------------|-----------|---------------------|
| **M1** | 2020 | 11 TOPS | 7-8 | First Apple Silicon with ML acceleration |
| **M1 Pro** | 2021 | 11 TOPS | 14-16 | More GPU cores for ML workloads |
| **M1 Max** | 2021 | 11 TOPS | 24-32 | Faster ML inference and training |
| **M1 Ultra** | 2022 | 22 TOPS | 48-64 | Dual M1 Max, massive parallel ML |
| **M2** | 2022 | 15.8 TOPS | 8-10 | Improved efficiency and ML performance |
| **M2 Pro** | 2023 | 15.8 TOPS | 16-19 | Enhanced ML processing |
| **M2 Max** | 2023 | 15.8 TOPS | 30-38 | Higher ML training capacity |
| **M2 Ultra** | 2023 | 31.6 TOPS | 60-76 | Designed for AI-heavy workloads |
| **M3** | 2023 | 18 TOPS | 10 | Hardware-accelerated ray tracing |
| **M3 Pro** | 2023 | 18 TOPS | 14-18 | More power-efficient ML performance |
| **M3 Max** | 2023 | 18 TOPS | 30-40 | Enhanced AI model training |
| **M4** | 2024 | 38 TOPS | 10-40 | MLX and AI optimizations |

* Networking
  * NVIDIA NVLink / InfiniBand
