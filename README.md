## Usage
* Use './seekDNS DOMAINNAME' to get the ip from the China DNS and World DNS.
* Use './whoiam DOMAINNAME' to fetch information of DOMAINAME.
* Use './isWhite IP' to assure whether it is in the white list.
## Example
We would like to find out whether `www.github.com` is in the subsets defined in `./cn.ipset`.
* Have a look at the DNS results from the world and China by './seekDNS www.github.com'
* Have a look at the DNS info of `www.github.com` by `./whoiam www.github.com`.
* Find out whether the IP from previous step is in the white list defined in `./cn.ipset` by `./isWhite IP`.
