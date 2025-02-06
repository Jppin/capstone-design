// App.js
import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import TabNavigator from "./navigation/TabNavigator";
import MedicineDetailScreen from "./screens/MedicineDetailScreen"; // 📌 상세보기 스크린 추가

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        {/* 하단 탭 네비게이션을 최상위로 추가 */}
        <Stack.Screen name="MainTabs" component={TabNavigator} />

        {/* 약품 상세 정보 페이지 (MedicineScreen에서 이걸 호출) */}
        <Stack.Screen
          name="MedicineDetail"
          component={MedicineDetailScreen}
          options={{ title: "약품 상세 정보" }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
