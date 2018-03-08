# net-diagnose 

A light tool to diagnose dns pollution


# Deployment

### Clone the project

```
    git clone https://github.com/FuQiFeiPian/net-diagnose.git
```

### Install dependencies

```
    sudo pip install [package]
```


### Usage

* Use `./seekDNS DOMAINNAME` to get the ip from the China DNS and World DNS.
* Use `./whoiam DOMAINNAME` to fetch information of DOMAINAME.
* Use `./isWhite IP` to assure whether it is in the white list.


### Example
We would like to find out whether `www.github.com` is in the subsets defined in `./cn.ipset`.
* Have a look at the DNS results from the world and China by './seekDNS www.github.com'
* Have a look at the DNS info of `www.github.com` by `./whoiam www.github.com`.
* Find out whether the IP from previous step is in the white list defined in `./cn.ipset` by `./isWhite IP`.



# Getting Started


### Prerequisites

* python is installed

### Running the tests

There is no unit tests written in this project, we will keep up when the project goes on

### Build

There is no build process in this project, we will keep up when the project goes on


# Logistics

### Contributing

Please read [CONTRIBUTING.md](https://github.com/FuQiFeiPian/net-diagnose/blob/master/docs/CONTRIBUTING.md) for contributing.
For details on our [code of conduct](https://github.com/FuQiFeiPian/net-diagnose/blob/master/docs/CODE_OF_CONDUCT.md), and the process for submitting pull requests to us.

### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the tags on this repository

### Authors

* **dorrywhale** - *Initial work* - [dorrywhale](https://github.com/dorrywhale)

See also the list of [contributors](https://github.com/FuQiFeiPian/net-diagnose/graphs/contributors) who participated in this project.

### Acknowledgments

See [Acknowledgments](https://github.com/FuQiFeiPian/net-diagnose/blob/master/docs/ACKNOWLEDGMENTS.md)


### License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/FuQiFeiPian/net-diagnose/blob/master/LICENSE.md) file for details


