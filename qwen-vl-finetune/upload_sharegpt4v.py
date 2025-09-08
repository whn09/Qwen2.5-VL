from huggingface_hub import HfApi, create_repo

# 初始化 API
api = HfApi()

# 创建数据集仓库（如果不存在）
repo_id = "whn09/sharegpt4v"
create_repo(repo_id, repo_type="dataset", exist_ok=True)

# 上传整个文件夹
api.upload_folder(
    folder_path="./sharegpt4v",
    repo_id=repo_id,
    repo_type="dataset",
    commit_message="Upload dataset files",
)
