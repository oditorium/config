# Config

_server configuration scripts for Ubuntu_

- `components` contains component installs
- `full` contains full server installs
- `_etc` contains configuration files


## Component Installs

*Component Installs* install specific server components. The file `000_init` is a basic
initialisation script for a new Ubuntu server. It should be run ahead of any other
component installs.

The component install files are pre-fixed with `100_` for basic components (in particular
programming languages), and `200_` for higher level components such as *Django*.


## Full Installs

*Full Installs* install a complete server. They pull in all necessary component installs
as needed, including `000_init`.
