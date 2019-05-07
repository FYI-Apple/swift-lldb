// main.swift
//
// This source file is part of the Swift.org open source project
//
// Copyright (c) 2018 Apple Inc. and the Swift project authors
// Licensed under Apache License v2.0 with Runtime Library Exception
//
// See https://swift.org/LICENSE.txt for license information
// See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
//
// -----------------------------------------------------------------------------
import Bar
import dylib

func use<T>(_ t: T) {}

func main() {
  let foo = FooToplevel(j: 42)
  f(foo) // break here
  use(foo)
}

main()
