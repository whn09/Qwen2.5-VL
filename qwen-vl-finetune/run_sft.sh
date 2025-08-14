source /opt/pytorch/bin/activate

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

sudo apt install -y ffmpeg
sudo apt install -y python3.12-dev

pip install -r requirements.txt

huggingface-cli download --repo-type dataset --resume-download lmms-lab/LLaVA-NeXT-Data --include llava_next_raw_format/ --local-dir LLaVA-NeXT-Data
cd LLaVA-NeXT-Data/llava_next_raw_format

for file in *.tar.gz; do
    tar -xzf "$file"
done

sh ./scripts/sft.sh
sh ./scripts/sft_7b.sh
sh ./scripts/sft_32b.sh