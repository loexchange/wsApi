package com.loex.service.signature;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.powermock.api.mockito.PowerMockito;
import org.powermock.core.classloader.annotations.PowerMockIgnore;
import org.powermock.core.classloader.annotations.PrepareForTest;
import org.powermock.modules.junit4.PowerMockRunner;

import static org.junit.Assert.assertEquals;

@RunWith(PowerMockRunner.class)
@PrepareForTest({ApiSignature.class})
@PowerMockIgnore({"javax.crypto.*"})
public class ApiSignatureTest {


  @Test
  public void testSignature() {

  }
}
