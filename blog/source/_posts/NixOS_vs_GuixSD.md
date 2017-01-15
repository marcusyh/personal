title: "Nix vs Guix, NixOS vs GuixDS"
date: 2017-01-14 05-15-00
tags:
---
[About Nix](http://nixos.org/nix/about.html)
[About NixOS](http://nixos.org/nixos/about.html)
[About NixOps -- The NixOS Cloud Deployment Tool](http://nixos.org/nixops/)
[The Nix Packages collection](http://nixos.org/nixpkgs/)
[Hydra is a Nix-based continuous build system](http://nixos.org/hydra/)
[Disnix is a distributed service deployment toolset](http://nixos.org/disnix/)

[Nix Package Manager Guide](http://nixos.org/nix/manual/)
[NixOS Manual](http://nixos.org/nixos/manual/)
[NixOps Manual](http://nixos.org/nixops/manual/)
[Nixpkgs Manual](http://nixos.org/nixpkgs/manual/)
[Hydra Manual](http://nixos.org/hydra/manual/)


[About Guix](https://www.gnu.org/software/guix/about/)
[GuixSD wikipedia](https://en.wikipedia.org/wiki/Guix_System_Distribution)
[GNU Guix Manual](https://www.gnu.org/software/guix/manual/)
[Service composition in GuixSD](http://savannah.gnu.org/forum/forum.php?forum_id=8412)


While Nix uses its own domain-specific language (DSL) to describe package composition, Guix embeds a DSL in the general-purpose language Scheme. This opens up new possibilities: Guix has several user interfaces (CLI, Emacs, and Web) written in Guile Scheme that have direct access to those package objects, maintenance tools such as 'guix lint' or 'guix refresh' similarly take advantage of that, and so on. GuixSD pushes integration further by using the same language and libraries in the initrd, boot scripts, init system, configuration management, and so on, rather than a mixture of independent projects, each with its own language and development environment. [link](https://lwn.net/Articles/665285/)

Comparing Guix and NixOS at hacker news: [link1](https://news.ycombinator.com/item?id=8246338) [link2](https://news.ycombinator.com/item?id=11410268) [link3](https://news.ycombinator.com/item?id=12337488) [link4](https://news.ycombinator.com/item?id=8965530)
Comparing Guix and NixOS at reddit: [link1](https://www.reddit.com/r/NixOS/comments/2n926h/get_best_of_both_worlds_guix_vs_nixos/) [link2](https://www.reddit.com/r/NixOS/comments/5nidt8/thanks_nixos/) [link3](https://www.reddit.com/r/NixOS/comments/49v0sr/is_there_a_nixos_docker_base_image/) 


Comparing Docker and NixOS:
-- [Why Docker is not the answer to reproducible research, and why Nix may be](https://blog.wearewizards.io/why-docker-is-not-the-answer-to-reproducible-research-and-why-nix-may-be)
-- [The case against Docker](https://www.andreas-jung.com/contents/the-case-against-docker)
-- [Stack + Nix = portable reproducible builds](http://www.tweag.io/blog/stack-nix-portable-reproducible-builds)
-- [A step towards the future of configuration and infrastructure management with Nix](http://container-solutions.com/step-towards-future-configuration-infrastructure-management-nix/)
-- [NixOS, Consul, Nginx and containers](http://lethalman.blogspot.com/2015/02/nixos-consul-nginx-and-containers.html)


[The Haskell Tool Stack](https://docs.haskellstack.org/en/stable/README/)


