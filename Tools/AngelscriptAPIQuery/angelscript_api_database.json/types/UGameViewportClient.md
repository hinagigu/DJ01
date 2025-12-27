# UGameViewportClient

**继承自**: `UScriptViewportClient`

A game viewport (FViewport) is a high-level abstract interface for the
platform specific rendering, audio, and input subsystems.
GameViewportClient is the engine's interface to a game viewport.
Exactly one GameViewportClient is created for each instance of the game.  The
only case (so far) where you might have a single instance of Engine, but
multiple instances of the game (and thus multiple GameViewportClients) is when
you have more than one PIE window running.

Responsibilities:
propagating input events to the global interactions list

@see UGameViewportClient

