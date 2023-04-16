import common
import os
import tempfile

def main():
    common.log("Iptables Advanced Firewall Configuration", log_type="~")
    
    iptables = "iptables"
    
    # Create a temporary file for saving current iptables rules
    rules_file = tempfile.NamedTemporaryFile(delete=False)
    rules_file.close()

    common.log("Backing up rules")
    common.execute([iptables, "-L", "-n"])  # Display current rules for reference
    common.execute(["iptables-save", ">", rules_file.name])

    common.log("Adding a test rule to the firewall")
    common.execute([iptables, "-A", "INPUT", "-p", "tcp", "--dport", "12345", "-j", "ACCEPT"])

    common.log("Displaying the modified rules")
    common.execute([iptables, "-L", "-n"])

    common.log("Restoring the original rules", log_type="-")
    common.execute(["iptables-restore", "<", rules_file.name])

    common.log("Displaying the restored rules")
    common.execute([iptables, "-L", "-n"])

    os.unlink(rules_file.name)  # Remove the temporary rules file

if __name__ == "__main__":
    exit(main())

