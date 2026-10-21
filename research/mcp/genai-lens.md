AWS Documentation from https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html:

# Generative AI Lens - AWS Well-Architected Framework

Publication date: **November 19, 2025** ([Document revisions](./document-revisions.html))

The AWS Well-Architected Generative AI Lens is an essential
resource for organizations seeking to harness the power of
generative AI technologies on AWS. As enterprises increasingly adopt
generative AI to drive innovation and solve advanced problems, they
require guidance and best practices to build applications that are
secure, efficient, scalable, and aligned with responsible AI
principles. This lens extends the Well-Architected Framework to
address the unique considerations and opportunities presented by
generative AI, empowering architects, developers, and
decision-makers to create solutions that maximize the potential of
these cutting-edge technologies.

By using this lens, you can gain a deep understanding of
how to design, deploy, and operate generative AI applications on AWS
effectively. The lens covers critical aspects of generative AI
systems, including operational excellence, security, reliability,
performance efficiency, cost optimization, and sustainability. It
provides actionable insights and recommendations across the entire
generative AI lifecycle, from scoping and model selection to
deployment and continuous improvement. Moreover, the lens emphasizes
the importance of responsible AI practices, considering the shared
responsibilities between model producers, providers, and consumers
in developing ethical and trustworthy AI systems.

Through the AWS Well-Architected Generative AI Lens, you can learn how to use AWS services and best practices to build
generative AI applications that are robust, secure, and
high-performing. Discover strategies for optimizing model
performance, maintaining data privacy and security, managing costs,
and promoting environmental sustainability. By applying the
principles and guidance provided in this lens, organizations can
confidently navigate the opportunities of generative AI and unlock
its transformative potential to drive business value and innovation.

The AWS Well-Architected Generative AI Lens provides guidance and
best practices for designing, deploying, and operating generative AI
applications on AWS. It extends the Well-Architected Framework to
address the unique considerations and opportunities of using
foundation models and generative AI technologies.

The lens covers key areas aligned with the Well-Architected pillars:

* **Operational excellence:** Achieve consistent model output quality,
  monitor and manage operational health, maintain traceability,
  automate lifecycle management, and determine when to execute
  model customization.
* **Security:** Protect generative AI endpoints, mitigate risks of
  harmful outputs and excessive agency, monitor and audit events,
  secure prompts and remediate model poisoning risks.
* **Reliability:** Handle throughput requirements, maintain reliable
  component communication, implement observability, handle
  failures gracefully, version artifacts, distribute inference,
  and verify completion of distributed computation tasks.
* **Performance efficiency:** Capture and improve model performance,
  maintain acceptable performance levels, optimize computation
  resources, and improve data retrieval performance.
* **Cost optimization:** Select cost-optimized models, balance cost
  and performance of inference, engineer prompts for cost,
  optimize vector stores and agent workflows.
* **Sustainability:** Minimize computational resources for training,
  customization, hosting, data processing, and storage. Leverage
  model efficiency techniques and serverless architectures.

It provides guidance across the generative AI lifecycle stages of
scoping, model selection, customization, development, deployment,
and continuous improvement. Responsible AI practices are
highlighted, considering shared responsibilities between model
producers, providers and consumers.

The lens aims to help architects, builders, and decision-makers
maximize the potential of generative AI on AWS while promoting
Well-Architected, secure, performant, and responsible solutions. It
provides a framework for evaluating and optimizing generative AI
workloads according to industry best practices.

## Scope

This document outlines Well-Architected best practices for
generative AI applications that use foundation models on Amazon Bedrock or customer-managed models on Amazon SageMaker AI. The
AWS Well-Architected Framework and lenses describe best practices in a
cloud- and technology-agnostic way. We present these best practices
and provide specific guidance on implementing these best practices
in their implementation steps.

This lens discusses best practices
for building business applications with Amazon Q, Amazon Bedrock,
and Amazon SageMaker AI. It provides guidance on architecting
generative AI solutions on AWS while adhering to the
Well-Architected Framework principles. The intended audience
includes architects, builders, security experts, MLOps engineers,
and decision-makers who are involved in designing, developing, and
operating generative AI applications on AWS. The document aims to
help these stakeholders understand how to maximize the potential of
generative AI while mitigating risks and building solutions that are
secure, reliable, performant, cost-effective, and sustainable.

For traditional machine learning (ML) applications built using Amazon SageMaker AI, see [Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html).

## Lens availability

Custom lenses extend the best practice guidance provided by AWS Well-Architected Tool. AWS WA Tool allows you to create your own
[custom
lenses](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-custom.html), or to use lenses created by others that have been
shared with you.

To begin reviewing your generative AI workload, download and import the [Generative AI Lens](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/generative-ai-lens/generative-ai-lens.json) into AWS Well-Architected Tool from the public [AWS Well-Architected custom lens GitHub repository](https://github.com/aws-samples/sample-well-architected-custom-lens).