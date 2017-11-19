cd /home/ubuntu/electionTools/bin
python ./moveFilesToDestination.py
python ./loadCVSfilesIntoDB.py
sudo python ./processVotationResults.py
