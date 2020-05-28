import docker
# client = docker.from_env()

# events = client.events()
# for event in events:
#     print(event)


class Connection(object):
    def __init__(self):
        client = docker.from_env()
        if client:
            self.state = "Accessible"
            self.client = client
        else:
            self.state = "Unaccessible"

    def status(self):
        return self.state

    def getList(self):
        print(self.client.containers.list())
        return self.client.containers.list(all=True)

    def getContainersDetail(self):
        containers = self.getList()
        return containers

    def runContainer(self, name, image, ports, env):
        try:
            self.client.run(image=image, name=name,
                            ports=ports, environment=env)
        except:
            print("error")


c = Connection()
print(c.getContainersDetail())
