/* config.h.  Generated automatically by configure.  */
/* config.h.in.  Generated automatically from configure.in by autoheader 2.13.  */

/* Define to empty if the keyword does not work.  */
/* #undef const */

/* Define as __inline if that's what the C compiler calls it.  */
/* #undef inline */

/* Define to `unsigned' if <sys/types.h> doesn't define.  */
/* #undef size_t */

/* Define if you have the ANSI C header files.  */
#define STDC_HEADERS 1

/* Use BSD User land PPP? */
/* #undef BSDUSER_PPP */

/* Use SLIRP? */
/* #undef SLIRP */

/* Let PPPD choose the IP addresses? */
/* #undef PPPD_IP_ALLOC */

/* Enable Broadcast Relay? */
/* #undef BCRELAY */

/* Work as a PNS rather than a PAC? */
/* #undef PNS_MODE */

/* Where is my pppd? */
#define PPP_BINARY "/usr/sbin/pppd"

/* Have libwrap? */
/* #undef HAVE_LIBWRAP */

/* Just #define to int if it's not defined */
/* #undef socklen_t */

/* These would be better as typedefs, but... */
/* #undef u_int8_t */
/* #undef u_int16_t */
/* #undef u_int32_t */

/* And the signed size_t */
/* (normal size_t is done by standard autoconf) */
/* #undef ssize_t */

/* Define if you have an openpty() (non-standard check) */
#define HAVE_OPENPTY 1

/* Define if you have the daemon function.  */
#define HAVE_DAEMON 1

/* Define if you have the fork function.  */
#define HAVE_FORK 1

/* Define if you have the getservbyname function.  */
#define HAVE_GETSERVBYNAME 1

/* Define if you have the memmove function.  */
#define HAVE_MEMMOVE 1

/* Define if you have the setproctitle function.  */
/* #undef HAVE_SETPROCTITLE */

/* Define if you have the setsid function.  */
#define HAVE_SETSID 1

/* Define if you have the strerror function.  */
#define HAVE_STRERROR 1

/* Define if you have the strlcpy function.  */
/* #undef HAVE_STRLCPY */

/* Define if you have the <libintl.h> header file.  */
#define HAVE_LIBINTL_H 1

/* Define if you have the <libutil.h> header file.  */
/* #undef HAVE_LIBUTIL_H */

/* Define if you have the <pty.h> header file.  */
#define HAVE_PTY_H 1

/* Define if you have the <string.h> header file.  */
#define HAVE_STRING_H 1

/* Define if you have the <syslog.h> header file.  */
#define HAVE_SYSLOG_H 1

/* Define if you have the c library (-lc).  */
#define HAVE_LIBC 1

/* Define if you have the intl library (-lintl).  */
/* #undef HAVE_LIBINTL */

/* Define if you have the nsl library (-lnsl).  */
#define HAVE_LIBNSL 1

/* Define if you have the socket library (-lsocket).  */
/* #undef HAVE_LIBSOCKET */

/* Define if you have the util library (-lutil).  */
#define HAVE_LIBUTIL 1

/* Name of package */
#define PACKAGE "pptpd"

/* Version number of package */
#define VERSION "1.1.3"

