from pimage import copy_move
from pimage.configuration import Configuration

configuration = Configuration(block_size=32)

fraud_list, ground_truth_image, result_image = copy_move.detect("../assets/anis1.jpg",
                                                                configuration=configuration,
                                                                verbose=True)

print(fraud_list)
print(ground_truth_image.size)
print(result_image.size)
