AWS Documentation from https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/amazon-sage-maker-ai-inference-endpoints.html:

# Amazon SageMaker AI inference endpoints

SageMaker AI Inference endpoints deliver a managed inference environment purpose-built for deploying foundation models (FMs) and other ML models at scale, while giving teams control over the underlying instances, inference engine, and optimization strategy.

## Infrastructure management

SageMaker AI manages the underlying ML instances while giving organizations control over instance types and configurations. The service handles instance provisioning, health monitoring, and infrastructure maintenance, so teams can focus on model deployment using containers maintained by AWS or custom containers. With [inference components](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-deploy-models.html), you can deploy multiple FMs to a single endpoint, allocate accelerators, CPU, and memory to each model individually, and independently add, update, or remove models that share the same underlying infrastructure. To accelerate scaling of large generative AI models, SageMaker AI offers [Container Caching](https://aws.amazon.com/blogs/machine-learning/introducing-container-caching-in-amazon-sagemaker-ai-for-faster-model-scaling/), which pre-cache container images to reduce response times during traffic spikes. To update models safely in production, [deployment guardrails](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html) provide controlled rollout options—including [blue/green](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-blue-green.html), canary, linear, and [rolling](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-rolling.html) deployments—with automatic rollback triggered by Amazon CloudWatch alarms to protect availability during endpoint updates.

## Pricing model

Customers are charged based on the instance types deployed, with costs covering both compute resources and storage. This instance-based [pricing model](https://aws.amazon.com/sagemaker/ai/pricing/) enables accurate cost forecasting based on instance selection and deployment duration. To optimize the cost of generative AI workloads with intermittent traffic, inference components can [scale down to zero](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-deploy-models.html) instances when idle and scale back up when requests arrive.

## Model architecture support

SageMaker AI provides access to hundreds of foundation models through [Amazon SageMaker JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html), including open-weight models such as Meta Llama, Mistral, DeepSeek, and Qwen, as well as NVIDIA NIM microservices, which you can deploy with a few clicks. The service also accommodates any compatible model framework or architecture, providing flexibility to deploy custom or fine-tuned generative AI models with PyTorch, vLLM, SGLang, or custom frameworks for multimodal and vision-language models.

## Automatic scaling

You can configure automatic scaling policies that adjust the number of instances or model copies based on multiple factors. For example, factors include time schedules, built-in Amazon CloudWatch metrics such as invocation rates, concurrent requests, and resource utilization, or framework-specific metrics like Time to First Token (TTFT) tailored to specific application requirements. With [capacity-aware inference and automatic instance fallback](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-heterogeneous.html), you can define a prioritized list of instance types (instance pools) so that SageMaker AI automatically provisions from the next available option when a preferred instance type has insufficient capacity, which improves resilience during endpoint creation, scale-out, and scale-in. Per-instance-type CloudWatch metrics provide visibility into latency, throughput, GPU utilization, and instance count by hardware type within a single endpoint.

## Inference engine choice

Teams can choose [AWS Deep Learning Containers](https://github.com/aws/deep-learning-containers) images that are optimized for popular frameworks and maintained by AWS. Alternatively, teams can bring custom container images that include specialized inference engines or dependencies.

## Inference optimizations and configurations

The service enables flexible configuration of both model parameters and system-level settings. Generative AI optimization techniques, including the following:

* Quantization to lower-precision data types, such as FP8 and AWQ, to reduce hardware requirements
* Speculative decoding, which accelerates text generation without sacrificing output quality
* Model sharding and tensor parallelism for distributing large models across multiple GPUs or Trainium NeuronCores
* Engine-specific strategies such as prefix caching

For many models, you can deploy [pre-optimized JumpStart models](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize-preoptimized.html) directly without running a separate optimization job. To identify the best deployment configuration, [optimized generative AI inference recommendations](https://docs.aws.amazon.com/sagemaker/latest/dg/generative-ai-inference-recommendations.html) automatically benchmark combinations of instance types (up to three at a time), serving containers, parallelism strategies, and optimization techniques on real GPU infrastructure against a performance goal (cost, latency, or throughput). You provide your model—base, custom, or fine-tuned, in Hugging Face/SafeTensors format from Amazon S3 or the SageMaker AI Model Registry—along with your expected token distributions and concurrency, and SageMaker AI returns deployment-ready configurations with validated metrics, such as time to first token (TTFT), inter-token latency (ITL), P50/P90/P99 request latency, throughput, and cost. You can also benchmark existing production endpoints to right-size over-provisioned infrastructure and reduce recurring inference spend.

## Supported clients and protocols

Applications can invoke endpoints through the Amazon SageMaker Runtime [API actions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_SageMaker_Runtime.html) over HTTPS, integrate using the AWS SDK, or use the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/) for streamlined Python-based interactions. SageMaker AI endpoints also expose an [OpenAI-compatible Chat Completions API](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-openai-compatible.html), so you can invoke models—including those hosted as inference components—from the OpenAI SDK or frameworks such as LangChain and Strands Agents by changing only the endpoint URL, using time-limited bearer tokens for authentication. For interactive generative AI applications, you can use [response streaming](https://aws.amazon.com/about-aws/whats-new/2023/09/sagemaker-real-time-inference-response-streaming/) with the `InvokeEndpointWithResponseStream` action to return tokens as they are generated, and [bidirectional streaming](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-bidi) over HTTP/2 to stream data continuously in both directions for real-time, full-duplex use cases such as voice agents, live transcription, and speech-to-text.