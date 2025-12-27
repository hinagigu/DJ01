# UMovieSceneEventSystem

**继承自**: `UMovieSceneEntitySystem`

Systems that triggers events based on one-shot FMovieSceneEventComponent components
Works by iterating all pending instances of TMovieSceneComponentID<FMovieSceneEventComponent> and triggering inline.
Does not dispatch any async tasks

