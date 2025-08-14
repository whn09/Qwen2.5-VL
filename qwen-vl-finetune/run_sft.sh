source /opt/pytorch/bin/activate

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

sudo apt install -y ffmpeg
sudo apt install -y python3.12-dev

cd /home/ubuntu
git clone https://github.com/whn09/Qwen2.5-VL
cd /home/ubuntu/Qwen2.5-VL/qwen-vl-finetune

pip install -r requirements.txt

cd /opt/dlami/nvme
huggingface-cli download --repo-type dataset --resume-download nyu-visionx/Cambrian-10M --local-dir Cambrian-10M
cd Cambrian-10M/
pip install natsort
python merge_tars.py
python extract.py
python check_images_exist.py

cd /opt/dlami/nvme
huggingface-cli download --repo-type dataset --resume-download FreedomIntelligence/ALLaVA-4V --local-dir ALLaVA-4V
cd ALLaVA-4V/allava_laion/image_chunks
for file in *.zip; do
    unzip "$file"
    rm -rf "$file"
done
mv images ../

cd /opt/dlami/nvme
huggingface-cli download --repo-type dataset --resume-download TIGER-Lab/VisualWebInstruct --local-dir VisualWebInstruct
cd VisualWebInstruct
unzip images.zip
rm -rf images.zip

cd /opt/dlami/nvme
huggingface-cli download --repo-type dataset --resume-download lmms-lab/LLaVA-NeXT-Data --include llava_next_raw_format/ --local-dir LLaVA-NeXT-Data
cd LLaVA-NeXT-Data/llava_next_raw_format
for file in *.tar.gz; do
    tar -xzf "$file"
    rm -rf "$file"
done

cd /opt/dlami/nvme
s5cmd cp Cambrian-10M s3://datalab/datasets/
s5cmd cp ALLaVA-4V s3://datalab/datasets/
s5cmd cp VisualWebInstruct s3://datalab/datasets/
s5cmd cp LLaVA-NeXT-Data s3://datalab/datasets/

cd /opt/dlami/nvme
s5cmd cp s3://datalab/datasets/Cambrian-10M Cambrian-10M
s5cmd cp s3://datalab/datasets/ALLaVA-4V ALLaVA-4V
s5cmd cp s3://datalab/datasets/VisualWebInstruct VisualWebInstruct
s5cmd cp s3://datalab/datasets/LLaVA-NeXT-Data LLaVA-NeXT-Data

cd /home/ubuntu/Qwen2.5-VL/qwen-vl-finetune
sh ./scripts/sft.sh
sh ./scripts/sft_7b.sh
sh ./scripts/sft_32b.sh