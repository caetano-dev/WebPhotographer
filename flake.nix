{
  description = "WebPhotographer";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs?ref=nixpkgs-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils }: {
    devShell = self.defaultPackage;
    defaultPackage.x86_64-linux =
      with import nixpkgs { system = "x86_64-linux"; };

      pkgs.python3Packages.buildPythonPackage rec {
        name = "WebPhotographer";
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
