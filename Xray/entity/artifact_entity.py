from dataclasses import dataclass
from torch.utils.data.dataloaders import DataLoader


@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str

    