"""
Tests ThreadSanitizer's support to detect a leaked thread.
"""

import os, time
import lldb
from lldbsuite.test.lldbtest import *
from lldbsuite.test.decorators import *
import lldbsuite.test.lldbutil as lldbutil
import json

class TsanThreadLeakTestCase(TestBase):

    mydir = TestBase.compute_mydir(__file__)

    @expectedFailureAll(oslist=["linux"], bugnumber="non-core functionality, need to reenable and fix later (DES 2014.11.07)")
    @skipIfFreeBSD # llvm.org/pr21136 runtimes not yet available by default
    @skipIfRemote
    @skipUnlessCompilerRt
    @skipIfDarwin  # rdar://25534884  TSAN tests failing on Green Dragon OS X CI (not not locally)
    def test (self):
        self.build ()
        self.tsan_tests ()

    def tsan_tests (self):
        exe = os.path.join (os.getcwd(), "a.out")
        self.expect("file " + exe, patterns = [ "Current executable set to .*a.out" ])

        self.runCmd("run")

        # the stop reason of the thread should be breakpoint.
        self.expect("thread list", "A thread leak should be detected",
            substrs = ['stopped', 'stop reason = Thread leak detected'])

        self.assertEqual(self.dbg.GetSelectedTarget().process.GetSelectedThread().GetStopReason(), lldb.eStopReasonInstrumentation)
