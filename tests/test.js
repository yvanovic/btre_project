import http from "k6/http";
import { check, sleep } from "k6";

// Test configuration
export const options = {
  thresholds: {
    // Assert that 99% of requests finish within 300ms.
    http_req_duration: [
      { threshold: "p(95) < 300", abortOnFail: true, delayAbortEval: "10s" },
    ],
  },
  // Ramp the number of virtual users up and down
  stages: [
    { duration: "30s", target: 5 },
    // { duration: "1m", target: 15 },
    // { duration: "20s", target: 0 },
  ],
};

// Simulated user behavior
export default function () {
  let res = http.get("https://test-api.k6.io/public/crocodiles/1/");
  // Validate response status
  check(res, { "status was 200": (r) => r.status == 200 });
  sleep(1);
}
