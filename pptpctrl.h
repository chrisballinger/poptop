/*
 * pptpctrl.h
 *
 * PPTP control function prototypes.
 *
 * $Id: pptpctrl.h,v 1.2 2011/05/19 00:02:50 quozl Exp $
 */

#ifndef _PPTPD_PPTPCTRL_H
#define _PPTPD_PPTPCTRL_H

extern int pptpctrl_debug;

#ifdef VRF
extern char *vrf;
#else
#define vrf_socket(vrf, dom, typ, prot) socket(dom, typ, prot)
#endif

#endif  /* !_PPTPD_PPTPCTRL_H */
