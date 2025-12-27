# UMovieSceneCachePreAnimatedStateSystem

**继承自**: `UMovieSceneEntityInstantiatorSystem`

System that becomes relevant if there are any entites tagged RestoreState,
or UMovieSceneEntitySystemLinker::ShouldCaptureGlobalState is true.
When run this system will iterate the instantiation phase in order, and call
IMovieScenePreAnimatedStateSystemInterface::Save(Global)PreAnimatedState on any
systems that implement the necessary interface

