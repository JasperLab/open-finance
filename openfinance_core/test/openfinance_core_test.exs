defmodule OpenfinanceCoreTest do
  use ExUnit.Case
  doctest OpenfinanceCore

  test "greets the world" do
    assert OpenfinanceCore.hello() == :world
  end
end
