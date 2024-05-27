let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (pp: with pp; [
      # check python3Packages attribute set in nix repl for list
      numpy
      pygame
      pyopengl
      pyopengl-accelerate
      mido # MIDI
    ]))
    #pkgs.rtmidi
  ];
}

