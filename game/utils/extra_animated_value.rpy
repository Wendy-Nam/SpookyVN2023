﻿
init -1499 python:

    @renpy.pure
    class ExtraAnimatedValue(AnimatedValue):
        """
        This extends AnimatedValue to allow:
            Querying of the current value at any point in time 
            Setting delay based on the full range
            Allowing a warper to control animation movement
            A few properties for returning current values
            Dynamic text displayables to track changing values

        :doc: value

        This animates a value, taking `delay` seconds to vary the value from
        `old_value` to `value`.

        `value`
         The value itself, a number.

        `range`
         The range of the value, a number.

        `delay`
         The time it takes to animate the value, in seconds. Defaults
         to 1.0.

        `range_delay`
         The time it takes to animate the value, in seconds across the full
         range. Overrides `delay` if set. Defaults to None

         `warper`
         String warper name to use to animate between values

        `old_value`
         The old value. If this is None, then the value is taken from the
         AnimatedValue we replaced, if any. Otherwise, it is initialized
         to `value`.
        """

        def __init__(self, value=0.0, range=1.0, delay=1.0, 
                           old_value=None, range_delay=None,
                           warper="linear"):
            if old_value == None:
                old_value = value

            self.value = value
            self.current_value = value
            self.range = range
            self.delay = delay
            self.range_delay = range_delay or None
            self.old_value = old_value
            self.start_time = None
            self.warper = warper

            self.adjustment = None

        @property
        def percent(self):
            """
            Percent expressed as a float between 0.0 and 1.0
            (suitable for use with PyFormat :.01% syntax)
            """
            return float(self.current_value) / float(self.range)

        def text(self, format="{.current_value:.0f}", **kwargs):
            return DynamicDisplayable(self.dynamic_text, 
                                      format=format, 
                                      **kwargs)

        def dynamic_text(self, st, at, **kwargs):
            value = kwargs.pop('format', "{.current_value:.0f}").format(self)
            delay = (0.1 if self.value == self.current_value else 0.02)
            return Text(value, **kwargs), delay

        def periodic(self, st):

            if self.range < self.value:
                self.value = self.range

            if self.start_time is None:
                self.start_time = st

            if self.value == self.old_value:
                return

            if self.range_delay is not None:

                self.delay = self.range_delay \
                           * ( abs(self.old_value - self.value) 
                               / float(self.range) )

            base_fraction = (st - self.start_time) / self.delay
            base_fraction = min(1.0, base_fraction)

            if base_fraction == 1.0:

                self.current_value = self.value

            else:

                fraction = renpy.atl.warpers[self.warper](base_fraction)

                self.current_value = self.old_value \
                                   + fraction * (self.value - self.old_value)

            self.adjustment.change(self.current_value)

            if base_fraction != 1.0:
                return 0







            ###########################################
            #                                         #
            #  A Displayable specifically designed    #
            #  to be used with ExtraAnimatedValue     #
            #  bars. Allowing dissolves between set   #
            #  images used for the bar components     #
            #                                         #
            ###########################################


init python:

    class ValueImage(renpy.Displayable):
        """
        A displayable that returns an image based on
        values taken from a reference object (ExtraAnimatedValue)

        @value_object:
            object that holds the relevant values 
            (.percent, .value, .current_value)
            the ExtraAnimatedValue object

        @images:
            the images 
            Either just image references or tuples of name and position
            "1.png", "2.png"
            ## will dissolve between 1.png and 2.png across the range
            or
            ("1.png", 0.0), ("2.png", 0.8), ("3.png", 1.0)
            # will dissolve between 1.png and 2.png across the first 80%
            # of range then dissolve between 2.png and 3.png across rest

        @kwargs:
            dissolve: boolean - default True
        """

        def __init__(self, value_object, *images, **kwargs):

            super(ValueImage, self).__init__(**kwargs)

            self.value_object = value_object

            self.images = list(images)

            for idx, i in enumerate(self.images):

                if not isinstance(i, (list, tuple)):

                    self.images[idx] = [
                        i, (float(idx) * (1.0 / (len(self.images) - 1)))]

                else:

                    self.images[idx] = list(self.images[idx])

                self.images[idx][0] = renpy.displayable(self.images[idx][0])

            self.dissolve = kwargs.get("dissolve", True)


        def render(self, width, height, st, at):

            self.old_value = getattr(self.value_object, "percent")

            layers = [self.images[0][0]]

            use_perc = self.old_value 

            for img, perc in self.images:

                if perc <= self.old_value:

                    layers[0] = img
                    use_perc = perc

                else:

                    if self.dissolve:

                        ratio = (float(self.old_value - use_perc) 
                                 / (perc - use_perc))

                        if ratio > 0.01:

                            layers.append(renpy.render(
                                Transform(img, alpha=ratio), 
                                width, height, st, at))

                    break

            layers[0] = renpy.render(layers[0], width, height, st, at)

            # Create the render we will return.
            render = renpy.Render(*layers[0].get_size())

            for k in layers:

                render.blit(k, (0, 0))

            if (getattr(self.value_object, "value") 
                != getattr(self.value_object, "current_value")):

                renpy.redraw(self, 0)

            # Return the render.
            return render


        def event(self, ev, x, y, st):

            return

        def visit(self):

            return [k[0] for k in self.images]
