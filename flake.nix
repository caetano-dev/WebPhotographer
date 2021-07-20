# {
#   description = "My flake";

#   inputs = {
#     nixpkgs.url = "github:NixOS/nixpkgs?ref=nixpkgs-unstable";
#     utils.url = "github:numtide/flake-utils";
#   };

#   outputs = { self, nixpkgs, utils }: (utils.lib.eachSystem ["x86_64-linux" ] (system: rec {

#     packages = {
#       pythonEnv = nixpkgs.legacyPackages.${system}.python3.withPackages(ps: with ps; [ selenium python-telegram-bot python-dotenv autopep8 ]);
#     };

#     defaultPackage = packages.pythonEnv; # If you want to juist build the environment
#     devShell = packages.pythonEnv.env; # We need .env in order to use `nix develop`
#   }));
# }

{
  description = "telegramBot";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs?ref=nixpkgs-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils }: {
    devShell = self.defaultPackage;
    defaultPackage.x86_64-linux =
      with import nixpkgs { system = "x86_64-linux"; };

      pkgs.python3Packages.buildPythonPackage rec {
        name = "telegramBot";
        src = ./.;
        propagatedBuildInputs = with pkgs.python3Packages; [
          selenium
          python-telegram-bot
          python-dotenv
          autopep8
        ];
      };
  };

}
