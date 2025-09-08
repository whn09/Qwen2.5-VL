from 763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:2.8.0-gpu-py312-cu129-ubuntu22.04-sagemaker

RUN apt update
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt install -y ffmpeg
RUN apt install -y python3.12-dev

RUN git clone https://github.com/whn09/Qwen2.5-VL

RUN cd Qwen2.5-VL/qwen-vl-finetune && pip install -r requirements.txt

RUN mkdir -p /opt/dlami/nvme

RUN cd /opt/dlami/nvme && hf download --repo-type dataset whn09/sharegpt4v --local-dir sharegpt4v && cd sharegpt4v && unzip sharegpt4v.zip

# RUN cd Qwen2.5-VL/qwen-vl-finetune && sh ./scripts/sft.sh
