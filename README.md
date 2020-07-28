# CelebA-Conditional-GAN
VAC+GAN for conditional generation

If you do not want to download the datatest zip file and the attribute file from http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html you can use the VAC+GAN+tfrec notebook. Doing so the dataset is loaded from a Google Cloud bucket. Please notice that it will be available on it till April 2021. If you prefer to load the datatest from tfrecords after that date you can use the celeba_tfrec script to create your tfrec files and upload them on a Google Cloud bucket that you prefer, then you have just to modify a little bit the notebook code by changing the path of the bucket.

In this kind of approach, the Generative Adversarial Network generator is turned into a conditional generator by placing a multi-class classifier in parallel with the discriminator network and backpropagate the classification error through the generator. This technique is versatile enough to be applied to any GAN [5].

# Just-Dance-NAO

**Team Name: Just Dance NAO** </br>

![Image description](JustDanceNao.jpg)

Fundamentals of Artificial Intelligence and Knowledge Representation </br>
NAO Planning Competition 2019 </br>

## Network

## Results

![Image description](JustDanceNao.jpg)

![Image description](JustDanceNao.jpg)

![Image description](JustDanceNao.jpg)



## Authors

**Simone Gayed Said** - simone.gayed@studio.unibo.it </br>
**Pierpasquale Colagrande** - pietro.obbiso@studio.unibo.it </br>

## References

**Special Movements** - https://funlab.nd.edu/the-nao-base/special-movements/ </br>
**Spotify playlist** - https://open.spotify.com/playlist/3nBdD3CigeiexPsubKnCxb?si=BkxprH0FSWOMZ9PjHQ9bkA


