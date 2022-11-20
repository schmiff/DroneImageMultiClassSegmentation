from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')
import cv2

class SegmentationDataLoader:
        """
        Takes the path to image/masks and creates a pandas dataframe with the given data
        """
        def __init__(self, image_folder_path: str, mask_folder_path: str) -> None:
                self.images = glob(image_folder_path)
                self.masks = glob(mask_folder_path)
                self.df = pd.DataFrame(data={"image_path": self.images, "mask_path":self.masks})

        def len(self):
                """
                Returns info about dataset
                """
                print(f'Dataset length: {len(self.df)}')






        def plot_examples(self, how_many=2):
                """
                Plot some example images from the dataset in a rows*columns grid
                """      
                print("Example image and mask pair")
                # Build Grid and load Images
                for i in range(0, how_many):
                        fig = plt.figure(figsize=(20,15))
                        img = cv2.imread(self.images[i])
                        mask = cv2.imread(self.masks[i])
                        plt.subplot(121)
                        plt.imshow(img)
                        plt.title("Image")
                        plt.subplot(122)
                        plt.imshow(mask)
                        plt.title("Mask")
                        plt.show()