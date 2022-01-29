
## Reference Material

 - [AWS EC2 Launch](https://www.amazonaws.cn/en/getting-started/tutorials/launch-a-virtual-machine/)
 - [Azure VM Launch](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/quick-create-portal)
 - [Google Cloud Platform VM Launch](https://cloud.google.com/compute/docs/instances/create-start-instance)

Follow [this video](https://youtu.be/i-Od-CELQoI) for live implementation of this problem statement.


### Steps :
#### AWS

1. Launch an Amazon EC2 Instance :
- Open Amazon EC2 console and then click Launch Instance to create and configure your virtual machine.

2. Configure your Instance
-  In this screen, you are shown options to choose an Amazon Machine Image (AMI). AMIs are preconfigured server templates you can use to launch an instance. Each AMI includes an operating system, and can also include applications and application servers.
- You will now choose an instance type. Instance types comprise of varying combinations of CPU, memory, storage, and networking capacity so you can choose the appropriate mix for your applications
- You can review the configuration, storage, tagging, and security settings that have been selected for your instance
- On the next screen you will be asked to choose an existing key pair or create a new key pair. A key pair is used to securely access your Linux instance using SSH. Amazon Web Services stores the public part of the key pair which is just like a house lock. You download and use the private part of the key pair which is just like a house key.

    Select Create a new key pair and give it the name MyKeyPair. Next click the Download Key Pair button.

    After you download the MyKeyPair key, you will want to store your key in a secure location. If you lose your key, you won't be able to access your instance. If someone else gets access to your key, they will be able to access your instance.

3. Connect to your Instance (either via SSH) 
4. Terminate Your Instance (go to the console and select the VM under actions and terminate)