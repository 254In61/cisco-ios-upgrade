#Bash Script that calls the different scripts involved.
#!/bin/bash
echo "IOS Upload process starting......"
./wr_iosVars.py
echo "Print out of recorded IOS Variables ...."
echo "=========================================="
cat modules/iosVars.yml
echo "=========================================="
echo ""
./cisco_iosUpload.yml --ask-vault-pass
