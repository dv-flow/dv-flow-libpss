import dataclasses as dc
from dv_flow.libpss.psp_log_parser import PspLogParser
from dv_flow.mgr import TaskMarker, TaskMarkerLoc, SeverityE
from typing import List

def test_smoke():
    snippet = """
   *** Error: Explicit import is not supported yet.
	[Suggestion: use wildcard import syntax if applicable]
		at line 2 in
/a/b/c/uart_tx_test.pss
import uart_c; // Import the component definition



   *** Error: No package called 'uart_c'
		at line 9 in
/a/b/c/pss_top/uart_tx_test.pss
            do uart_c::Config with {



   *** Error: No package called 'uart_c'
		at line 17 in
/a/b/c/uart_tx_test.pss
                do uart_c::TxChar with {


   *** Error: 3 load errors were detected.
"""

    @dc.dataclass
    class Context(object):
        markers : List = dc.field(default_factory=list)

        def marker(self, msg, severity, loc):
            self.markers.append(TaskMarker(
                msg=msg,
                severity=severity,
                loc=loc
            ))

    ctxt = Context()
    psp_log_parser = PspLogParser(ctxt)

    for line in snippet.splitlines():
        psp_log_parser.line(line)
    psp_log_parser.line("")

    assert len(ctxt.markers) == 3
    assert ctxt.markers[0].msg == "Explicit import is not supported yet. [Suggestion: use wildcard import syntax if applicable]"
    assert ctxt.markers[0].loc is not None
    assert ctxt.markers[0].loc.path == "/a/b/c/uart_tx_test.pss"
    assert ctxt.markers[0].loc.line == 2
    assert ctxt.markers[1].msg == "No package called 'uart_c'"
    assert ctxt.markers[1].loc is not None
    assert ctxt.markers[1].loc.path == "/a/b/c/pss_top/uart_tx_test.pss"
    assert ctxt.markers[1].loc.line == 9
    assert ctxt.markers[2].msg == "No package called 'uart_c'"
    assert ctxt.markers[2].loc is not None
    assert ctxt.markers[2].loc.path == "/a/b/c/uart_tx_test.pss"
    assert ctxt.markers[2].loc.line == 17