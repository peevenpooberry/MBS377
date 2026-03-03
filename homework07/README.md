# Homework 7: *Databases and APIs*

### Components of directory:
+ docker-compose.yml: Upon a `Docker compose -d` command Docker will start up a Redis database container in the background
+ get_nbci_genbank_records.py: A program file that will use the Redis database container to store results from API requests to the NCBI Protein database
+ ./ouput_files/: The directory where results saved to the Redis database will be shown via text files.

### How to use the program
1. Make sure the system is running Docker, installation documentation can be found [here](https://docs.docker.com/engine/install/).
2. To make a Redis database on your machine, we can use the service `reddis-db` within the docker-compose.yml, to start this service use the command:
   ```
   docker compose -f path/to/docker-compose.yml up -d
   [+] Running 1/1
    ✔ Container redis  Started   
   ```
   Next we can check the status of Redis

   ```
   $ docker ps
   CONTAINER ID   IMAGE     COMMAND                  CREATED      STATUS      PORTS                                         NAMES
   cf46a8e12299   redis     "docker-entrypoint.s…"   2 days ago   Up 2 days   0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp   redis

3. The program file depends on the Python modules: [Biopython.Entrez](https://biopython.org/docs/1.76/api/Bio.Entrez.html), [Biopython.SeqIO](https://biopython.org/docs/1.76/api/Bio.SeqIO.html),
   and [redis](https://pypi.org/project/redis/), which must all be accessible to the Python interpreter.
5. Now we can use the program file get_ncbi_genbank_records.py
   To run we can use the command `./get_ncbi_genbank_records.py` and by default we will see an output file called records.txt containing the results of a search of
   "Arabidopsis thaliana AND AT5G10140".

   This program however is customizable from the console and by using flags we can change the output and function.
   + `-l` allows us to change the logging level when running the program with options DEBUG, INFO, WARNING, ERROR, with the default being WARNING
   + `-o` changes the name of the output file, but names must end in the file format .txt
   + `-s` contains the search request that is sent to the NCIB Protein Database, the default is "Arabidopsis thaliana AND AT5G10140"
