from torchvision.datasets.folder import ImageFolder
import os.path as osp
# from .imagelist import ImageList
# from ._util import download as download_data, check_exits


class Food32(ImageFolder):
    def __init__(self, root, split='train', transform=None, download=True):
        # list(map(lambda file_name, _: check_exits(root, file_name), self.download_list))
        super(Food32, self).__init__(osp.join(root, split), transform=transform)
        self.num_classes = 32
    
    CLASSES = [str(i) for i in range(32)] # masked classes
    
    @classmethod
    def get_classes(self):
        return Food32.CLASSES