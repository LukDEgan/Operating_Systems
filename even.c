#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <unistd.h>

void sigint_handler(int signal) {
  if (signal == SIGINT) printf("Yeah!\n");
  if (signal == SIGHUP) printf("Ouch!\n");
}

void set_signal_action(void) {
  // Declare the sigaction structure
  struct sigaction act;

  // Set all of the structure's bits to 0 to avoid errors
  // relating to uninitialized variables...
  bzero(&act, sizeof(act));
  // Set the signal handler as the default action
  act.sa_handler = &sigint_handler;
  // Apply the action in the structure to the
  // SIGINT signal (ctrl-c)
  sigaction(SIGINT, &act, NULL);
  sigaction(SIGHUP, &act, NULL);
}
int main(int argc, char* argv[]) {
  set_signal_action();
  int n = atoi(argv[1]);
  for (int i = 0; i < n; i++) {
    sleep(5);
    printf("%d\n", i * 2);
  }
}