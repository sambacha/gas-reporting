import { FastifyReply } from 'fastify';

export function sendInvalidParamError(res: FastifyReply, param: string) {
  res.status(500).send({
    success: false,
    error: 'Internal Server Error',
    message: `Missing or invalid ${param} parameter`,
  });
}

export function sendErrorMessage(res: FastifyReply, error: Error) {
  res.status(500).send({
    success: false,
    error: 'Internal Server Error',
    message: error.message,
  });
}
