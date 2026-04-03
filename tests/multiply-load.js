import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '10s', target: 5 },
    { duration: '20s', target: 10 },
    { duration: '10s', target: 0 },
  ],
};

export default function () {
  const url = 'http://127.0.0.1:5000/api/multiply';

  const payload = JSON.stringify({
    matrix1: [[1, 2], [3, 4]],
    matrix2: [[5, 6], [7, 8]]
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const res = http.post(url, payload, params);

  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 1000 ms': (r) => r.timings.duration < 1000,
  });

  sleep(1);
}