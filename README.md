<p><div align="center"><img src="https://github.com/exec-bypass/elemental-attack/raw/master/images/97.png" width=200px style="align:center;" /></div></p>

## Elemental
Elemental is a centralized threat library of MITRE ATT&CK techniques, Atomic Red Team tests, and over 280 Sigma rules. It provides an alternative way to explore the ATT&CK dataset, mapping relevant Atomic Red Team tests and Sigma rules to their respective technique. Elemental allows defenders to create custom ATT&CK Techniques and upload Sigma Rules. The ATT&CK dataset was collected via the hunters-forge attackcti Python client. Atomic Red Team tests were imported from the Atomic Red Team GitHub repository. Sigma rules were imported from Sigma's GitHub rule collection if they contained ATT&CK tags.

This platform was conceived as a capstone project for University of California Berkeley's Master of Information and Cybersecurity program. We look forward to community feedback for new ideas and improvements. This instance of Elemental is experimental and not configured for production deployment. Please see Django documentation on configuring a production server.

## Features
+ View ATT&CK Technique information
+ View Atomic Red Team tests in Markdown and Yaml
+ View Sigma rules in Yaml
+ Add new ATT&CK Techniques (currently only available from Django Admin panel)
+ Upload new Sigma rules (currently only available from Django Admin panel)

## Screenshots
<p>
<div>
  Main Elements View
  <br />
  <img src="https://github.com/exec-bypass/elemental-attack/blob/master/images/elementalUI.png" width=900px style="align:center;" />
</div>
</p>
<p>
<div>
  Technique View
  <br />
  <img src="https://github.com/exec-bypass/elemental-attack/raw/master/images/Technique.png" width=900px style="align:center;" />
</div>
</p>
<p>
<div>
  Atomics View
  <br />
  <img src="https://github.com/exec-bypass/elemental-attack/raw/master/images/AtomicYaml.png" width=900px style="align:center;" />
</div>
</p>
<p>
<div>
  <img src="https://github.com/exec-bypass/elemental-attack/blob/master/images/Atomic.png" width=900px style="align:center;" />
</div>
  </p>
<p>
<div>
  Sigma Rules View
  <br />
  <img src="https://github.com/exec-bypass/elemental-attack/blob/master/images/Sigma.png" width=900px style="align:center;" />
</div>
</p>

## Installation
git clone https://github.com/exec-bypass/elemental-attack.git

cd Elemental/elemental

pip install -r requirements.txt

python manage.py runserver

Default Django admin page crendentials:  user: elemental |  password: berkelium

## Thanks
Mitre ATT&CK - https://github.com/mitre/cti

Atomic Red Team - https://github.com/redcanaryco/atomic-red-team

ATT&CK Python Client - https://github.com/hunters-forge/ATTACK-Python-Client

Sigma - https://github.com/Neo23x0/sigma

## TODO
- [ ] Log Source mapping for Techniques and Sigma rules
- [ ] Custom Techniques add
- [ ] Custom Sigma Rules upload
- [ ] Sigmac to convert rules to desired SIEM
- [ ] Filter capabilities on Elements page
- [ ] Integrate update functionality for ATT&CK, Atomic Red Team, and Sigma rules repo

## Authors
* Josh Hakala (<a href="https://github.com/exec-bypass">exec-bypass</a>)
* Steve Rice (<a href="https://github.com/sdrice">sdrice</a>)
* Aaron Crouch (<a href="https://github.com/TTwoONEsiXX">TTwoONEsiXX</a>)
* Erick Pasco (<a href="https://github.com/epasco5">epasco5</a>)

## License
Please see license file
