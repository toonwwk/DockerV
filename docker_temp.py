import docker

class User():
    def __init__(self):
        self.client = docker.from_env()
        self.setup()

    def setup(self):
        self.image_list = self.client.images.list()

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

    
        


