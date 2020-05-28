import docker

class User():
    def __init__(self):
        self.client = docker.from_env()
        self.setup()

    def setup(self):
        self.image_list = self.client.images.list()
        self.volume_list = self.client.volumes.list()

    def addImage(self, image):
        self.image_list.append(image)

    def pullImage(self, repository):
        try:
            return self.client.images.pull(repository)
        except:
            return False  

    def getContainersList(self):
        return self.client.containers.list()

    def getImagesList(self):
        return self.image_list
    
    def getNumberOfImageList(self):
        return len(self.image_list)
    
    def getImageID(self, index) -> str:
        return self.image_list[index].id

    def getImageTags(self, index) -> str:
        image =  self.image_list[index]
        image_tags = image.tags[0]
        return image_tags[0:image_tags.rfind(':')]

    def getImageSize(self, index) -> int:
        image =  self.image_list[index]
        image_size = image.attrs['Size']
        return image_size

    def getImageCreatedDate(self, index) -> str:
        image =  self.image_list[index]
        image_created_date = image.attrs['Created']
        return image_created_date

    def getImageDetail(self, index) -> list:
        return [self.getImageID(index), self.getImageTags(index),\
                str(self.getImageSize(index)), self.getImageCreatedDate(index)]
    
    def removeImage(self, image):
        self.client.images.remove(image, True, True)

    def getVolumeList(self):
        return self.volume_list

    def addVolumeToList(self, volume):
        self.volume_list.append(volume)

    def getVolumeID(self, index) -> str:
        return self.volume_list[index].id

    def removeVolume(self, volume):
        volume.remove(force = True)

    def getVolumeMountPoint(self, index) -> str:
        volume = self.volume_list[index]
        return volume.attrs['Mountpoint']
        
    def getVolumeDriver(self, index) -> str:
        volume = self.volume_list[index]
        return volume.attrs['Driver']

    def getVolumeCreatedDate(self, index) -> str:
        volume = self.volume_list[index]
        return volume.attrs['CreatedAt']

    def addVolume(self, name):
        try: 
            new_volume = self.client.volumes.create(name)
            self.addVolumeToList(new_volume)
            return new_volume
        except:
            return False


    
        


