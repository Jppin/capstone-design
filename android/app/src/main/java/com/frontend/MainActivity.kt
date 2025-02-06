package com.frontend

import com.facebook.react.ReactActivity
import com.facebook.react.ReactActivityDelegate
import com.facebook.react.defaults.DefaultNewArchitectureEntryPoint.fabricEnabled
import com.facebook.react.defaults.DefaultReactActivityDelegate
import com.swmansion.gesturehandler.react.RNGestureHandlerEnabledRootView // 👈 추가

class MainActivity : ReactActivity() {

  override fun getMainComponentName(): String = "Frontend"

  override fun createReactActivityDelegate(): ReactActivityDelegate =
      object : DefaultReactActivityDelegate(this, mainComponentName, fabricEnabled) {
          override fun createRootView(): RNGestureHandlerEnabledRootView { // 👈 추가
              return RNGestureHandlerEnabledRootView(this@MainActivity)
          }
      }
}
