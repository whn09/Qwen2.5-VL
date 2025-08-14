import re

# Define placeholders for dataset paths
CAMBRIAN_737K = {
    "annotation_path": "PATH_TO_CAMBRIAN_737K_ANNOTATION",
    "data_path": "",
}

CAMBRIAN_737K_PACK = {
    "annotation_path": f"PATH_TO_CAMBRIAN_737K_ANNOTATION_PACKED",
    "data_path": f"",
}

MP_DOC = {
    "annotation_path": "PATH_TO_MP_DOC_ANNOTATION",
    "data_path": "PATH_TO_MP_DOC_DATA",
}

CLEVR_MC = {
    "annotation_path": "PATH_TO_CLEVR_MC_ANNOTATION",
    "data_path": "PATH_TO_CLEVR_MC_DATA",
}

VIDEOCHATGPT = {
    "annotation_path": "PATH_TO_VIDEOCHATGPT_ANNOTATION",
    "data_path": "PATH_TO_VIDEOCHATGPT_DATA",
}

CAMBRIAN10M = {
    "annotation_path": "/opt/dlami/nvme/Cambrian-10M/jsons/Cambrian10M.jsonl",
    "data_path": "/opt/dlami/nvme/Cambrian-10M/",
}

LLAVANEXT = {
    "annotation_path": "/opt/dlami/nvme/LLaVA-NeXT-Data/llava_next_raw_format/llava_next_raw_format_processed.json",
    "data_path": "/opt/dlami/nvme/LLaVA-NeXT-Data/llava_next_raw_format/",
}

ALLaVA4V = {
    "annotation_path": "/opt/dlami/nvme/ALLaVA-4V/allava_laion/ALLaVA-Instruct-LAION-4V.json",
    "data_path": "/opt/dlami/nvme/ALLaVA-4V/",
}

VISUALWEBINSTRUCT = {
    "annotation_path": "/opt/dlami/nvme/VisualWebInstruct/visualwebinstruct_qa.jsonl",
    "data_path": "/opt/dlami/nvme/VisualWebInstruct/",
}

data_dict = {
    "cambrian_737k": CAMBRIAN_737K,
    "cambrian_737k_pack": CAMBRIAN_737K_PACK,
    "mp_doc": MP_DOC,
    "clevr_mc": CLEVR_MC,
    "videochatgpt": VIDEOCHATGPT,
    "cambrian_10m": CAMBRIAN10M,
    "llava_next": LLAVANEXT,
    "allava_4v": ALLaVA4V,
    "visualwebinstruct": VISUALWEBINSTRUCT,
}


def parse_sampling_rate(dataset_name):
    match = re.search(r"%(\d+)$", dataset_name)
    if match:
        return int(match.group(1)) / 100.0
    return 1.0


def data_list(dataset_names):
    config_list = []
    for dataset_name in dataset_names:
        sampling_rate = parse_sampling_rate(dataset_name)
        dataset_name = re.sub(r"%(\d+)$", "", dataset_name)
        if dataset_name in data_dict.keys():
            config = data_dict[dataset_name].copy()
            config["sampling_rate"] = sampling_rate
            config_list.append(config)
        else:
            raise ValueError(f"do not find {dataset_name}")
    return config_list


if __name__ == "__main__":
    dataset_names = ["cambrian_737k"]
    configs = data_list(dataset_names)
    for config in configs:
        print(config)
