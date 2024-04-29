import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path =r'C:\Users\Loaner13\Desktop\Computer vision project\exp\results.csv'

data_metrics = pd.read_csv(file_path)
# print(data_metrics)
columns= data_metrics.columns
# get epochs
epochs= list(data_metrics[columns[0]])
# print(epochs)
# get train loss
train_loss_box=list(data_metrics[columns[1]])
# print(f'train_loss_box:{train_loss_box}')
# print('**********************************************')
train_loss_obj=list(data_metrics[columns[2]])
# print(f'train_loss_obj:{train_loss_obj}')
# print('**********************************************')



# get validation loss
validation_loss_box=list(data_metrics[columns[7]])
# print(f'validation loss_box:{validation_loss_box}')
# print('**********************************************')


validation_loss_obj=list(data_metrics[columns[8]])
# print(f'validation_loss_obj:{validation_loss_obj}')

# create plotsa
plt.plot(epochs, train_loss_obj, label='Train Object Loss')
plt.plot(epochs, validation_loss_obj, label='validation object Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Train and validation Object Loss vs Epochs')
plt.legend()
plt.savefig('trian and validation object loss.jpg')
plt.show()


plt.plot(epochs, train_loss_box, label='train Box Loss')
plt.plot(epochs, validation_loss_box, label='validation Box Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Box Loss vs Epochs')
plt.legend()
plt.savefig('trianand validation  box loss.jpg')
plt.show()




