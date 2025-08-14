source /opt/pytorch/bin/activate

pip install -r requirements.txt

huggingface-cli download --repo-type dataset --resume-download lmms-lab/LLaVA-NeXT-Data --include llava_next_raw_format/ --local-dir LLaVA-NeXT-Data
cd LLaVA-NeXT-Data/llava_next_raw_format

for file in *.tar.gz; do
    tar -xzf "$file"
done

sh ./script/sft.sh
sh ./script/sft_7b.sh
sh ./script/sft_32b.sh