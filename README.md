# Innosilicon A10 Model Changer
Tool to change the model of the A10 Innosilicon Miners. 

It appears that Innosilicon are charging people to upgrade their boards to another version. 
The internal API of the Innosilicon is what is used to do this. 

To run this tool, I have included a compiled Windows EXE (a10_change_model.exe) for you. 
 
The steps are:
1. Run the a10_change_model.exe tool. 
2. Enter your Username and Password for the miner (default is admin / admin). 
3. Enter the IP Address of the miner. 
4. Press 1 to change model. 
5. Select model: 
- A10L - 5 GB RAM - 3 Hash boards each with 8 Chips
- A10U - 6 GB RAM - 3 Hash boards each with 8 Chips
- A10S - 5 GB RAM - 4 Hash boards each with 9 Chips
- A10X - 6 GB RAM - 4 Hash boards each with 9 Chips
6. Once the tool closes, go to the website of your miner and login. 
7. Go to Overview and confirm the Type is the model you want to change to. 
8. Go to Firmware and upload the firmware file from Innosilicon that matches the model. 
9. Once rebooted, check the Overview page and confirm both the Type and Platform Version match your model. 

Once this is complete, you are now fully updated and ready to go. 


I have noticed the following layout of RAM for the chips:

**7GB**

 - U5 K4Z80325BC 1GB
 - U6 K4ZAF325BM 2GB 
 -  U7 K4ZAF325BM 2GB 
 - U8 K4ZAF325BM 2GB

**6GB**

 - U5 K4Z80325BC 1GB
 - U6 K4Z80325BC 1GB
 - U7 K4ZAF325BM 2GB
 - U8 K4ZAF325BM 2GB


**5GB**

 - U5 K4Z80325BC 1GB
 - U6 K4Z80325BC 1GB
 - U6 K4Z80325BC 1GB
 - U8 K4ZAF325BM 2GB

**4GB**

 - U5 K4Z80325BC 1GB
 - U6 K4Z80325BC 1GB
 - U6 K4Z80325BC 1GB
 - U8 K4Z80325BC 1GB

I have included a photo thanks to @funkyfeel of the chip location. 

If this saves you a ton of money, please consider donating. 

Ethereum: 0xB55d55fB887Bea10fEB0f7E13DD3Ff91f1767ef9

Tron: TNtWj62WSDHBEKHu4bwv927vGHgp89A1CN
