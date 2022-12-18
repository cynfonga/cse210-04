def _init_(self ,keyboard_service,video_service):
    self._keyboard_service=keyboard_serviceself.video_service=video_service
    self._points=0



def start_game(self,cast):
    self._video_service.open_window()
    while self.video_service.is_window_open():
        self._do_updates(cast)
        self._do_outputs(cast)
        self._video_service.close_windows


def _get_inputs(self,cast):
    robot=cast.get_first_actor("robots")
    velocity=self._keyboard_service.get_direction()
    robot.set_velocity(velocity)


def _do_updates(self,cast):

    banner=cast.get_first_actor("banners")
    robot=cast.get_first_actor("robot")
    artifacts=cast.get_actors("artifacts")
    max_X=self._video_service.get_width()
    max_Y=self._video_service.get_height()
    robot.move_next(max_X,max_Y)
            
